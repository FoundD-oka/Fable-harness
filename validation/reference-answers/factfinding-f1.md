# Fable（私）のF1封印回答 — codex実行前

## 「SAML SSO でログインできる？」

結論から言うと、**今のliveでは使えない。「対応」と書いてあるけど実態は"コードはあるが未接続"**。

コードを追った事実：
- README には「SAML SSO 対応」とある
- `auth.py` に `sso_login()` は実装されてる
- でも `config.py` は `FEATURES["sso"] = False`（本番で無効）
- しかも `routes.py` の `login_route` は `password_login` しか呼んでなくて、**SSO経路がそもそもルーティングされてない**

だから状態としては「一部ある／live未反映」。ドキュメントの記述だけを信じると事故る。

次の判断：もしSSOを実際に使いたいなら、必要なのは (1) `FEATURES["sso"]` を有効化、
(2) `login_route`（またはルータ）に SSO ディスパッチを追加、の2つ。今は「SSO対応済み」
ではなく「**UI/コードはあるが運用未接続**」として扱うのが安全。
