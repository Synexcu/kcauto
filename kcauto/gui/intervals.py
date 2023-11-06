import PySimpleGUI as sg
import subprocess
import os

from gui.layout_base import LayoutBase
from gui.config_methods import ConfigMethods
from util.json_data import JsonData


class Intervals(LayoutBase):
    DEF_PATH = os.path.join(os.getcwd(), 'configs', 'config.json')
    JSON_FILETYPE = ('JSON file', '*.json')
    INITIAL_CONFIG_FOLDER = 'configs'

    @classmethod
    def get_layout(cls):
        intervals = cls.load_intervals()
        sleep_modifier = (
            intervals['sleep_modifier'] if 'sleep_modifier' in intervals else '')
        loop_break = (
            intervals['loop_break_seconds']
            if 'loop_break_seconds' in intervals
            else cls.autodetect_python())
        instant = (
            intervals['instant'] if 'instant' in intervals else True)
        debug_output = (
            intervals['debug_output'] if 'debug_output' in intervals else False)
        return sg.Column(
            [
                [
                    sg.Text(f'Sleep Modifier', **cls.LABEL_SETTINGS),
                    sg.InputText(
                        sleep_modifier,
                        key=f'gui.sleep_modifier',
                        font=cls.FONT_10,
                        size=(50, 1),
                        enable_events=True),
                    sg.FileBrowse(
                        'load',
                        key='load_cfg_sleep',
                        font=cls.FONT_8,
                        button_color=cls.COLORS_STANDARD_BUTTON,
                        file_types=(cls.JSON_FILETYPE, ),
                        initial_folder=cls.INITIAL_CONFIG_FOLDER,
                        target='gui.sleep_modifier')
                ],
                [
                    sg.Text('Put a comma (,) for every second(s) you typed. e.g. (0,1,2,21,50,75,100)',
                            **cls.LABEL_INTERVALS,
                            pad=((135, 0), (0, 10))),
                ],
                [
                    sg.Text('P.S. Modifying Sleep Modifier when used in a config where a choice node is available',
                            **cls.LABEL_INTERVALS,
                            pad=((135, 0), (0, 0))
                            )
                ],
                [
                    sg.Text('is',
                            **cls.LABEL_INTERVALS,
                            pad=((135, 0), (0, 10))
                            ),
                    sg.Text('NOT RECOMMENDED.',
                            **cls.LABEL_INTERVALS,
                            pad=((0, 0), (0, 10)),
                            text_color='red'
                            ),
                    sg.Text('Using Instant Sleep Modifier is ADVISED. (0 seconds only).',
                            **cls.LABEL_INTERVALS,
                            pad=((0, 0), (0, 10))
                            ),
                ],
                [
                    sg.Text('', **cls.LABEL_SETTINGS),
                    sg.Button(
                        'Save & overwrite',
                        pad=((0, 0), (0, 20)),
                        key='save_intervals_sleep'),
                    sg.FileSaveAs(
                        'Save as',
                        key='save_as',
                        font=cls.FONT_10,
                        pad=((1, 0), (0, 20)),
                        target='save_cfg_path',
                        file_types=(cls.JSON_FILETYPE, ),
                        initial_folder=cls.INITIAL_CONFIG_FOLDER)
                ],
                
                ### PAD

                [
                    sg.Text(f'Loop Break Modifier', **cls.LABEL_SETTINGS),
                    sg.InputText(
                        loop_break,
                        key=f'gui.loop_break_seconds',
                        font=cls.FONT_10,
                        size=(50, 1),
                        enable_events=True),
                    sg.FileBrowse(
                        'load',
                        key='load_cfg_loop',
                        font=cls.FONT_8,
                        button_color=cls.COLORS_STANDARD_BUTTON,
                        target='gui.loop_break_seconds')
                ],
                [
                    sg.Text('Put a comma (,) for every second(s) you typed. e.g. (0,1,2,21,50,75,100)',
                            **cls.LABEL_INTERVALS,
                            pad=((135, 0), (0, 20))),
                ],
                [
                    sg.Text('', **cls.LABEL_SETTINGS),
                    sg.Button(
                        'Save  & overwrite',
                        pad=((0, 0), (0, 20)),
                        key='save_intervals_loop'),
                    sg.FileSaveAs(
                        'save as',
                        key='save_as',
                        font=cls.FONT_10,
                        pad=((1, 0), (0, 20)),
                        target='save_cfg_path',
                        file_types=(cls.JSON_FILETYPE, ),
                        initial_folder=cls.INITIAL_CONFIG_FOLDER)
                ],
                [
                    sg.Text('', **cls.LABEL_SETTINGS),
                    sg.Checkbox(
                        'Instant Sleep Modifier',
                        default=instant,
                        key='gui.instant',
                        pad=((0, 20), (0, 0)),
                        enable_events=True),
                    sg.Checkbox(
                        'Instant Loop Break Modifier',
                        default=debug_output,
                        key='gui.debug_output',
                        enable_events=True),
                ],
                [
                    sg.Text('Overrides both operations above and sets everything to 0 seconds.',
                            **cls.LABEL_INTERVALS,
                            pad=((135, 0), (0, 20))),
                ],
                # [
                #     sg.Text('', **cls.LABEL_SETTINGS),
                #     sg.Button(
                #         'Save',
                #         key='save_intervals'),
                # ]
            ],
            key='gui_tab_intervals',
            size=cls.PRIMARY_COL_TAB_SIZE,
            visible=False
        )

    def load_intervals():
        try:
            intervals = JsonData.load_json('gui_intervals.json')
            return intervals
        except FileNotFoundError:
            return {}

    def save_intervals_sleep(values):
        intervals = {
            'sleep_modifier': values['gui.sleep_modifier']
        }
        JsonData.dump_json(intervals, 'gui_intervals.json', pretty=True)

    def save_intervals_loop(values):
        intervals = {
            'loop_break_seconds': values['gui.loop_break_seconds']
        }
        JsonData.dump_json(intervals, 'gui_intervals.json', pretty=True)

    def autodetect_python():
        for cmd in (('python', ), ('python3', ), ('py', '-3')):
            output = subprocess.run([*cmd, '--version'], capture_output=True)
            if (
                    output.stdout
                    and output.stdout.decode('utf-8').split(' ')[1][0] == '3'):
                return ' '.join(cmd)
        return ''

    @classmethod
    def update_gui(cls, window, event, values):
        elements = (
            'gui.sleep_modifier',
            'gui.loop_break_seconds')
        
        if event == 'save_intervals_sleep':
            cls.save_intervals_sleep(values)

        if event == 'save_intervals_loop':
            cls.save_intervals_loop(values)

        # if event == 'autodetect_python':
        #     window['gui.loop_break_seconds'].Update(cls.autodetect_python())
    
    @staticmethod
    def update_cfg_filename(window, path):
        window['cfg_filename'].Update(os.path.basename(path))

    @staticmethod
    def save_cfg(path, window, values):
        cfg = ConfigMethods.generate_config_dict(window, values)
        JsonData.dump_json(cfg, path, pretty=True)

    @staticmethod
    def load_cfg(path, window, event, values):
        cfg = JsonData.load_json(path)
        ConfigMethods.unpack_config_dict(window, cfg)
