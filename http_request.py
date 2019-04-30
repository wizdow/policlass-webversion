class Request:

    method = ''
    request = ''
    host = ''
    connection = ''
    user_agent = ''
    accept = ''
    referer = ''
    accept_encoding = ''
    accept_language = ''
    cookie = ''
    data = []

    def __init__(self, data):
        self.data = data

        request = data.split('\r\n').pop(0)
        data = data.split(' ')

        self.request = 'index.html' if data[1].lstrip('/') == '' else data[1].lstrip('/')
        self.method = data[0]

        for parameter in request:
            parameter = parameter.lower()
            if 'host: ' in parameter:
                self.host = parameter.replace('host: ', '')
                break
            elif 'connection: ' in parameter:
                self.connection = parameter.replace('connection: ', '')
                break
            elif 'user-agent: ' in parameter:
                self.user_agent = parameter.replace('user-agent: ', '')
                break
            elif 'accept: ' in parameter:
                self.accept = parameter.replace('accept: ', '')
                break
            elif 'referer: ' in parameter:
                self.referer = parameter.replace('referer: ', '')
                break
            elif 'accept-encoding: ' in parameter:
                self.accept_encoding = parameter.replace('accept-encoding: ', '')
                break
            elif 'accept-language: ' in parameter:
                self.accept_language = parameter.replace('accept-language: ', '')
                break
            elif 'cookie: ' in parameter:
                self.cookie = parameter.replace('cookie: ', '')
                break
            else:
                continue

    def get_request(self):
        return self.request

    def get_data(self):
        return self.data

    def set_request(self, request):
        self.request = request

    def set_data(self, data):
        self.data = data
