class AttrDisplay:
    '''
    Реализует наследственный метод перегрузки операции вывода, отбржающий имена
    классов экземпляров и все фтрибуты в виде пар имя=значение, имеющиеся в экземплярах (исключая атрибуты, унаследованные 
    от классов). Может добовляться в любые классы и работать с любыми экземплярами.
    
    '''
    
    def getherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('{}={}'.format(key, getattr(self, key)))
        return ', '.join(attrs)
    def __str__(self):
        return '[{} {}]'.format(self.__class__.__name__, self.getherAttrs())

if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
        
    class SubTest(TopTest):
        pass
        
    x, y = TopTest(), SubTest()
    print(x)
    print(y)

