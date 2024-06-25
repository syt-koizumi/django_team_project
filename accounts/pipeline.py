def set_user_data(backend, strategy, details, response, user=None, *args, **kwargs):
  """
  SNS認証時にプロバイダから取得したデータをプロフィールに設定する
  """
  if backend.name == "line":
    # ユーザー名を取得。取得できなかった場合はuserIdをユーザー名とする。
    username = response.get("displayName", response["userId"])

  else:
    # Twitterの場合はscreen_nameを使用
    username = response.get("displayName", response["screen_name"])


  user.username = username
  user.save()