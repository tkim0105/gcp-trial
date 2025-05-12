
echo "環境変数のチェックを行います..."

if [ -n "$GOOGLE_CREDENTIALS_JSON" ]; then
    echo "GOOGLE_CREDENTIALS_JSON は設定されています。"
    GOOGLE_STATUS="設定済み"
else
    echo "GOOGLE_CREDENTIALS_JSON は設定されていません。"
    GOOGLE_STATUS="未設定"
fi

if [ -n "$PULUMI_ACCESS_TOKEN" ]; then
    echo "PULUMI_ACCESS_TOKEN は設定されています。"
    PULUMI_STATUS="設定済み"
else
    echo "PULUMI_ACCESS_TOKEN は設定されていません。"
    PULUMI_STATUS="未設定"
fi

echo ""
echo "チェック結果のサマリー:"
echo "------------------------"
echo "GOOGLE_CREDENTIALS_JSON: $GOOGLE_STATUS"
echo "PULUMI_ACCESS_TOKEN: $PULUMI_STATUS"

if [ "$GOOGLE_STATUS" = "設定済み" ] && [ "$PULUMI_STATUS" = "設定済み" ]; then
    echo "すべての必要な環境変数が設定されています。"
    exit 0
else
    echo "一部の必要な環境変数が設定されていません。"
    exit 1
fi
