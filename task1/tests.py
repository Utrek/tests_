def test_function (function,expected,*args):
    result = function(*args)
    try:
        assert result == expected 
        print(f"Тест функции {function.__name__} с аргументами {args} пройден успешно")
    except AssertionError as e:
        print(f"Тест функции {function.__name__} с аргументами {args} провален")
        

