# multi_match
dmdict
======
背景与应用场景
--------------
将lib库中的ul_dictmatch进行了python封装，从而能方便进行多模匹配。

使用方法
--------
可以参考test_dm.py进行使用

    创建一个词典
        import dmdict
        d = dmdict.DMSearchDict()

    添加词条
        d.add( lemma )
        d.add( lemma, prop )

    母串查找
        for lemma, begin, length, prop in d.find( long_text ):
            # do something.

    序列化
        d.save(output_filename)
        d.load(input_filename)

