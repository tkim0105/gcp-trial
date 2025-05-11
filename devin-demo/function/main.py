"""Cloud Functions用のシンプルなHello Worldモジュール。"""

import logging

logging.basicConfig(level=logging.INFO)


def hello_world(request):
    """
    シンプルなHello Worldを返すCloud Functionです。

    この関数は以下の処理を行います：
    1. ログに挨拶メッセージを出力
    2. 挨拶メッセージをレスポンスとして返却

    Args:
        request: HTTPリクエストオブジェクト

    Returns:
        str: 挨拶メッセージを文字列として返却
    """
    message = "Hello, World!"
    logging.info("Devin demo: %s", message)

    return message
