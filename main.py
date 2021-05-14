import tkinter as tk


class Application(tk.Frame):
    # entry用変数
    entry = None

    # 入力検証に失敗した場合に呼ばれる関数
    def invalidText(self):
        print('だめ!大文字入力!絶対！！')

    # 入力検証するための関数
    # 入力された文字に対して入力検証を行う。
    # 入力された文字が大文字ならば、"入力不正"とみなし、entry Widget内へ入力された文字を追加しない。
    # 入力された文字が大文字ならば、ブザーを鳴らす。
    def onValidate(self, d, i, P, s, S, v, V, W):
        ################################################################
        # 入力検証のために、利用できるデータ内容をtext Widgetへ書き込む。
        # d : テキストボックスを操作したアクション内容(1=insert(文字を追加した), 0=delete(文字を削除した), -1(その他))
        # i : 現在テキストボックスに格納される、文字列の長さ + 1(文字列indexの長さ)
        # P : 現在テキストボックスに格納される、文字列。
        # s : 現在テキストボックスに格納される、1つ前の文字列。
        # S : テキストボックスを操作した時の文字(挿入/削除する文字)
        # v : entry Widget内で宣言される、validateの値
        # V : 操作することでトリガーされた、validateの値(key, focusin, focusout, forced)(トリガーとは? : https://wa3.i-3-i.info/word12308.html)
        # W : 現在利用中のWidgetの種類
        ################################################################

        # 前回入力された内容を全て破棄する。
        # 1.0 : 先頭
        # end : 末尾
        self.text.delete("1.0", "end")

        self.text.insert("end", "OnValidate:\n")
        # 今回入力されるデータを挿入する。
        # end : 末尾
        self.text.insert("end", "d='%s'\n" % d)
        self.text.insert("end", "i='%s'\n" % i)
        self.text.insert("end", "P='%s'\n" % P)
        self.text.insert("end", "s='%s'\n" % s)
        self.text.insert("end", "S='%s'\n" % S)
        self.text.insert("end", "v='%s'\n" % v)
        self.text.insert("end", "V='%s'\n" % V)
        self.text.insert("end", "W='%s'\n" % W)

        ################################################################

        # 入力された文字が小文字の場合
        if S == S.lower():
            return True
        # 入力された文字が大文字の場合
        else:
            # 入力不正のブザーを鳴らす。
            self.bell()
            return False

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        self.master.geometry("300x200")

        ############################################## frame Widget START ##############################################

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        ############################################## frame Widget END ##############################################

        ############################################## text Widget START ##############################################

        # frame Widget(Frame)を親要素として、入力検証のために、利用できるデータ内容を書き込むtext Widgetを作成する。
        # height : 高さの設定
        # width : 幅の設定
        self.text = tk.Text(frame, height=10, width=40)

        # frame Widget(Frame)を親要素とした場合に、text Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.text.pack()

        ############################################## text Widget END ##############################################

        ############################################## entry Widget START ##############################################

        # 入力検証するための関数登録と、入力検証するために必要なデータ宣言を行う。
        # register : 入力検証用関数の登録を行う。
        # self.onValidate : 入力検証用関数
        #
        # %d = テキストボックスを操作したアクション内容(1=insert(文字を追加した), 0=delete(文字を削除した), -1(その他))
        # %i = 現在テキストボックスに格納される、文字列の長さ + 1(文字列indexの長さ)
        # %P = 現在テキストボックスに格納される、文字列。
        # %s = 現在テキストボックスに格納される、1つ前の文字列。
        # %S = テキストボックスを操作した時の文字(挿入/削除する文字)
        # %v = entry Widget内で宣言される、validateの値
        # %V = 操作することでトリガーされた、validateの値(key, focusin, focusout, forced)(トリガーとは? : https://wa3.i-3-i.info/word12308.html)
        # %W = 現在利用中のWidgetの種類
        vCmd = (self.register(self.onValidate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # width : 幅の設定
        # validate : 入力検証するオプションの値を設定。
        # validatecommand : 入力検証用関数の設定。
        # invalidcommand : 入力検証により、入力不正が発生した場合に呼ばれる関数の設定。
        ##################################### validateのオプションの種類 ###############################################
        # none : 入力検証しない。
        # focus : entry Widgetへカーソルがあたった、カーソルが外れた場合に入力検証する。
        # focusin : entry Widgetへカーソルがあたった場合に入力検証する。
        # focusout : entry Widgetへカーソルが外れた場合に入力検証する。
        # key : entry Widgetへ文字の追加、削除が行われた場合に入力検証する。
        # all : focus, focusin, focusout, key全て。
        ############################################################################################################
        self.entry = tk.Entry(frame, width=15, validate="key", validatecommand=vCmd, invalidcommand=self.invalidText)

        # frame Widget(Frame)を親要素とした場合に、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.entry.pack()

        ############################################## entry Widget END ##############################################

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    app.mainloop()
