class EthereumException(Exception):
    def __init__(self, description=None):
        self.description = '以太坊交易错误'
        if description:
            self.description = description


class EthereumRPCError(EthereumException):
    def __init__(self, description):
        self.description = description if description else'以太坊RPC连接错误'


class BalanceException(EthereumException):
    def __init__(self, value=None, balance=None):
        if balance is not None and value is not None:
            self.description = '余额不足：%s ether < %s ether' % (balance, value)
        elif value:
            self.description = '余额不足： < %s ether' % value
        else:
            self.description = '余额不足'
