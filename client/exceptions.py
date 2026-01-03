class RPCServerNotFound(ConnectionRefusedError):

    def __init__(self, msg, code):
        super().__init__(msg)
        self.msg = msg
        self.code = code