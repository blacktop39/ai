from src import main

def test_main_runs():
    try:
        main.main()
    except Exception as e:
        assert False, f"main() 실행 중 에러 발생: {e}"
