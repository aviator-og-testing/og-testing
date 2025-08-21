#!/usr/bin/env python3
"""Test script to verify typer import and dependencies."""

import sys

def test_typer_installation():
    """Test typer installation and all sub-dependencies."""
    print("=== Typer Dependency Installation Test ===\n")
    
    try:
        # Test main typer import
        import typer
        print("✓ Typer import successful")
        print(f"✓ Typer version: {typer.__version__}")
        
        # Test typer sub-dependencies
        import click
        print(f"✓ Click (typer dependency) version: {click.__version__}")
        
        # Test other common typer sub-dependencies
        try:
            import rich
            print(f"✓ Rich (optional typer dependency) version: {rich.__version__}")
        except ImportError:
            print("○ Rich not installed (optional dependency)")
        
        try:
            import shellingham
            print(f"✓ Shellingham (typer dependency) version: {shellingham.__version__}")
        except ImportError:
            print("○ Shellingham not found (optional dependency)")
            
        # Test basic typer functionality
        app = typer.Typer()
        print("✓ Typer app creation successful")
        
        # Test typer decorator functionality
        @app.command()
        def test_command(name: str = "World"):
            return f"Hello {name}!"
            
        print("✓ Typer command decorator works")
        
        print("\n🎉 All typer dependencies are correctly resolved!")
        print("✓ Installation test PASSED")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("✗ Typer is not installed or not available")
        print("Run: pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_typer_installation()
    sys.exit(0 if success else 1)