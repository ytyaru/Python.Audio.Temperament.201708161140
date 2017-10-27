#https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E
#http://www.chaco2008.com/theory/1-3_majorscale.html
#http://www.chaco2008.com/theory/2-3_minorscale.html
#メジャー・スケール=全,全,半,全,全,全,半
#マイナー・スケール=全,半,全,全,半,全,全
#全音=2, 半音=1
#CMajor=C,D,E,F,G,A,B
#Cminor=C,D,D#,F,G,G#,A#
#メジャースケールの次に重要かも？
#http://jazzpianopractice.net/theory/melodicminor
#https://www.joey-web.com/jazz/Theory/melodicminorscale.html
#ナチュラル・マイナー・スケールの♭6と♭7を半音上げたスケール。ジャズやフュージョンなどで多く使われる。
class MelodicMinorScale:
    def __init__(self):
        # ナチュラル・マイナー・スケールにおける__aeolian_intervalsの最後の一つ前の要素を半音上げたものと同じ
        self.__aeolian_intervals = [2,1,2,2,1,3,2]
#        self.__names = ['Aeolian', 'Locrian', 'Ionian', 'Dorian', 'Phrigian', 'Lydian', 'Mixolydian']
#        self.__names = ['Melodic', 'Dorian', ]
        # メジャースケールにSuperをつけたのと同じ
        self.__names = ['SuperIonian', 'SuperDorian', 'SuperPhrigian', 'SuperLydian', 'SuperMixolydian', 'SuperAeolian', 'SuperLocrian']
        self.__index = 0
        self.__intervals = [2,1,2,2,1,3,2]

    @property
    def Index(self): return self.__index
    @property
    def Name(self): return self.__names[self.__index]
    @property
    def Intervals(self): return self.__intervals
    
    def GetIntervalsFromName(self, name):
        print('name', name)
        if name not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
#        if name.title() not in self.__names: raise Exception(f'nameは{self.__names}のいずれかにしてください。')
        index = self.__GetIntervalsIndex(name)
        return self.GetIntervalsFromIndex(index)
    def GetIntervalsFromIndex(self, base_index):
        if base_index < 0 or len(self.__names) <= base_index: raise Exception('base_indexは0〜{len(self.__names)-1}の整数値にしてください。')
        self.__index = base_index
        self.__intervals.clear()
        self.__intervals.extend(self.__aeolian_intervals[base_index:])
        self.__intervals.extend(self.__aeolian_intervals[:base_index])
#        print(self.__names[base_index], self.__intervals)
        return self.__intervals
    def __GetIntervalsIndex(self, name):
        for i, n in enumerate(self.__names):
            if name.title() == self.__names[i].title(): return i
        return -1


if __name__ == '__main__':
    s = MelodicMinorScale()
    print('========== メロディック・マイナー・スケール ==========')
    print('---------- index ----------')
    for index in range(len(s.Intervals)):
        s.GetIntervalsFromIndex(index)
        print(index, s.Index, s.Name, s.Intervals)
    print('---------- name ----------')
    for name in ['SuperIonian', 'SuperDorian', 'SuperPhrigian', 'SuperLydian', 'SuperMixolydian', 'SuperAeolian', 'SuperLocrian']:
        s.GetIntervalsFromName(name)
        print(s.Index, s.Name, s.Intervals)
