pythonとpython, pythonとnodejsによるRPC（リモートプロシージャコール）の実装

clientはjsonデータを送信しjsonデータに基づき、指定の関数により値を受け取る。
リクエスト形式
{
   "method": 関数名, 
   "params": [値, 値], 
   "param_types": [型, 型], 
   "id": id_number
}
serverはclientからjsonデータを受け取り、関数を実行した値をjsonデータに変換してclientにレスポンスする。
レスポンス形式
{
   "results": 値,
   "result_type": 型,
   "id": id_number
}

サーバー側に備わっている関数
・floor(double x): 10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
・nroot(int n, int x): 方程式 rn = x における、r の値を計算する。
・reverse(string s): 文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
・validAnagram(string str1, string str2): 2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
・sort(string[] strArr): 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。

