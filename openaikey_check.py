import openai

# OpenAI APIキーを設定
api_key = "SET_YOUR_API_KEY"  # ここにあなたのAPIキーを入力してください
openai.api_key = api_key

def check_api_key_validity():
    try:
        # 簡単なリクエストを送信して、キーが有効か確認
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        )
        print("APIキーは有効です。リクエストが成功しました。")
    except openai.error.AuthenticationError:
        print("APIキーが無効です。正しいキーを設定してください。")
    except openai.error.OpenAIError as e:
        print(f"OpenAI APIのエラーが発生しました: {e}")
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")

# APIキーの有効性をチェック
check_api_key_validity()