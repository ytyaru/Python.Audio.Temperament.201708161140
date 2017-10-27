# このソフトウェアについて

平均律とピタゴラス音律でKey=C(ハ長調)の各種音階(Scale)の構成音を算出した。

基音440Hz。Keyを変えて算出することもできるが、全パターンだと膨大なファイル数(864)になってしまうため避けた。音階も民族系は外した。

```
音律(2) * 調(1) * 音階(9) = 18種
```

さらにファイル形式(4)もあるため`4 * 18 = 72`ファイルある。

コードも鳴らしたかったが、コードのパターンも膨大なので網羅しづらい。

# 対象ファイル名

ファイル名|説明
----------|----
makeTemperamentAndChord2.py|平均律とピタゴラス音律でKey=C(ハ長調)の各種音階(Scale)の構成音を音声ファイルに出力する
MusicTheory/temperament/PythagoreanTuning.py|ピタゴラス音律

# 実行

`res/`配下に音声ファイルを出力する。

```sh
$ python src/makeTemperamentAndChord2.py
---------- EqualTemperament ----------
BaseFrequency: 440 Hz
[440.0, 466.1637615180899, 493.8833012561241, 523.2511306011972, 554.3652619537442, 587.3295358348151, 622.2539674441618, 659.2551138257398, 698.4564628660078, 739.9888454232688, 783.9908719634985, 830.6093951598903]
********** EqualTemperament 440Hz **********
======= Major =======
----- C -----
======= Minor =======
----- C -----
======= Diminished =======
----- C -----
======= HarmonicMinor =======
----- C -----
======= MelodicMinor =======
----- C -----
======= MajorPentaTonic =======
----- C -----
======= MinorPentaTonic =======
----- C -----
======= BlueNote =======
----- C -----
======= Chromatic =======
----- C -----
---------- PythagoreanTuning ----------
BaseFrequency: 440 Hz
[440, 463.5390946502056, 495.0, 521.4814814814814, 556.875, 586.6666666666666, 626.484375, 660.0, 695.3086419753085, 742.5, 782.2222222222222, 835.3125]
********** PythagoreanTuning 440Hz **********
======= Major =======
----- C -----
======= Minor =======
----- C -----
======= Diminished =======
----- C -----
======= HarmonicMinor =======
----- C -----
======= MelodicMinor =======
----- C -----
======= MajorPentaTonic =======
----- C -----
======= MinorPentaTonic =======
----- C -----
======= BlueNote =======
----- C -----
======= Chromatic =======
----- C -----
```

# 課題

* 和音パターンを調査し網羅したい
* 12平均律以外の音律でも構成音を算出したいが……
    * 純正律における中間の5音も算出したい。計算方法がよくわからない
* ソースコードが整理できていない
    * 音楽理論がわからず、どうまとめていいのかもわからない

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

## 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

## 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

## 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

### 五度圏

* http://dn-voice.info/music-theory/godoken/

## 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

## サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

