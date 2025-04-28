from utils.path_manager import PathManager
from utils.code_fixer import CodeFixer

def setup_project():
    """Initialize project structure and verify setup."""
    print("\n🚀 Setting up Trading Agent project...")
    
    # Initialize utilities
    path_manager = PathManager()
    fixer = CodeFixer()
    
    # Run auto-fix to check dependencies and structure
    fixer.auto_fix()
    
    # Verify paths
    data_dir = path_manager.get_path('data')
    memory_file = path_manager.get_file_path('memory', 'trading_history.pkl')
    
    print(f"\n📁 Project Structure:")
    print(f"  Data Directory: {data_dir}")
    print(f"  Memory File: {memory_file}")
    
    return True

if __name__ == "__main__":
    setup_project()
    print("\nRunning tests...")
    import os
    os.system("cd c:\\Users\\hp\\Desktop\\TradingAgent")
    os.system("python setup.py")
    os.system("python -m unittest tests\\test_agent.py -v")