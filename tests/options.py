def pytest_addoption(parser):
    group = parser.getgroup('is-ecp-gis')

    group.addoption(
        '--browser', dest='browser', metavar='browser', default='chrome', help='Browser. Default option is chrome'
    )

    group.addoption(
        '--ui_url',
        help='A way to override the ui_url for your tests.',
        metavar='ui_url',
        default='smart-id.mos.ru/iam/auth/realms/smart/protocol/openid-connect/auth?response_type=code'
        '&client_id=secure-login&redirect_uri=https://smart.mos.ru/main/',
    )

    parser.addoption(
        '--remote_ip',
        help='A way to set remote url of selenoid',
        dest='remote_ip',
        metavar='remote_ip',
        # default='internal:Xai6eedaeGhepeiwoh5M@cview-bal1p.passport.local',
        default='selenoid1.kdc',
    )

    parser.addoption(
        '--remote_port',
        help='A way to set remote port of selenoid',
        dest='remote_port',
        metavar='remote_port',
        default='4444',
    )

    parser.addoption(
        '--remote_ui',
        help='A way to set remote url of selenoid ui',
        dest='remote_ui',
        metavar='remote_ui',
        # default='internal:Xai6eedaeGhepeiwoh5M@cview-bal1p.passport.local',
        default='selenoid1.kdc',
    )

    parser.addoption(
        '--wait',
        help='(int) Value waiting of condition in seconds',
        dest='wait',
        metavar='wait',
        type=int,
        default=30,
    )

    parser.addoption(
        '--enable-video',
        action='store',
        dest='enable_video',
        type=bool,
        default=False,
        help='Enable recording video option',
    )

    parser.addoption(
        '--block-urls',
        action='store',
        dest='block_urls',
        type=bool,
        default=False,
        help='Block request urls',
    )

    parser.addoption('--user', action='store', dest='username', type=str, default='ivanov_fm2', help='Username')
    parser.addoption('--password', action='store', dest='password', type=str, default='DXwl7p1', help='Password')
