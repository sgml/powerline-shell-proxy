def add_root_indicator_segment():
    root_indicators = {
        'bash': ' \\$ ',
    #    'bash': '',
        'zsh': ' \\$ ',
        'bare': ' > ',
    }
    bg = Color.PATH_BG
    #bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG
    if powerline.ret != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG
    powerline.append(root_indicators[powerline.shell], fg, bg)

powerline.register( add_root_indicator_segment )
