"""
環境変数のチェックを行うスクリプト
"""
import os
import sys

def check_env_vars():
    """必要な環境変数が設定されているかチェックします。"""
    required_vars = ["GOOGLE_CREDENTIALS_JSON", "PULUMI_ACCESS_TOKEN"]
    missing_vars = []
    status = {}
    
    for var in required_vars:
        if os.environ.get(var):
            status[var] = "設定済み"
        else:
            status[var] = "未設定"
            missing_vars.append(var)
    
    print("環境変数のチェックを行います...")
    for var, stat in status.items():
        print(f"{var}: {stat}")
    
    print("\nチェック結果のサマリー:")
    print("------------------------")
    for var, stat in status.items():
        print(f"{var}: {stat}")
    
    if missing_vars:
        print(f"一部の必要な環境変数が設定されていません: {', '.join(missing_vars)}")
        return False
    else:
        print("すべての必要な環境変数が設定されています。")
        return True

if __name__ == "__main__":
    success = check_env_vars()
    sys.exit(0 if success else 1)
