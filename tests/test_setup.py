import pytest
import importlib
import sys
import setuptools

def test_setup_configuration(monkeypatch):
    """
    Test that the setup() function in setup.py is called with the correct configuration arguments.
    
    This test monkeypatches setuptools.setup to capture the keyword arguments passed
    to it when setup.py is imported. It then checks that the package configuration details,
    such as 'name', 'version', 'install_requires', and 'entry_points', are as expected.
    """
    captured_kwargs = {}
    def dummy_setup(*args, **kwargs):
        nonlocal captured_kwargs
        captured_kwargs = kwargs
    # Replace setuptools.setup with dummy_setup to capture the configuration.
    monkeypatch.setattr(setuptools, 'setup', dummy_setup)
    # Remove 'setup' module from sys.modules if already imported to force re-execution.
    if 'setup' in sys.modules:
        del sys.modules['setup']
    # Import the setup.py module, which will call the dummy_setup function.
    import setup  # noqa: F401
    # Verify that the configuration values were captured.
    assert 'name' in captured_kwargs, "Expected 'name' to be in the setup configuration."
    assert captured_kwargs['name'] == 'bigfun', "Package name should be 'bigfun'."
    assert 'version' in captured_kwargs, "Expected 'version' to be in the setup configuration."
    assert captured_kwargs['version'] == '0.1.0', "Package version should be '0.1.0'."
    assert 'packages' in captured_kwargs, "Expected 'packages' to be in the setup configuration."
    assert 'bigfun' in captured_kwargs['packages'], "Package list should include 'bigfun'."
    expected_install_requires = [
        'google-cloud-bigquery',
        'google-cloud-bigquery_connection',
        'pyyaml',
        'jinja2',
        'mkdocs-material',
        'click',
        'click-help-colors',
    ]
    assert 'install_requires' in captured_kwargs, "Expected 'install_requires' in the configuration."
    assert captured_kwargs['install_requires'] == expected_install_requires, "Install requires do not match expected values."
    assert 'entry_points' in captured_kwargs, "Expected 'entry_points' to be in the configuration."
    entry_points = captured_kwargs['entry_points']
    assert 'console_scripts' in entry_points, "Expected 'console_scripts' in entry_points."
    console_scripts = entry_points['console_scripts']
    # Verify that the console script entry point for 'bigfun' is included.
    assert any('bigfun = bigfun.cli:cli' in script for script in console_scripts), \
        "Console scripts should include 'bigfun = bigfun.cli:cli'."

def test_package_data_and_include_package_data(monkeypatch):
    """
    Test that the package_data and include_package_data configurations in setup.py
    are correctly set.
    """
    captured_kwargs = {}
    def dummy_setup(*args, **kwargs):
        nonlocal captured_kwargs
        captured_kwargs = kwargs
    # Replace setuptools.setup with dummy_setup to capture the configuration.
    monkeypatch.setattr(setuptools, 'setup', dummy_setup)
    # Remove 'setup' module from sys.modules if already imported to force re-execution.
    if 'setup' in sys.modules:
        del sys.modules['setup']
    # Import the setup.py module, which will call dummy_setup.
    import setup  # noqa: F401
    # Verify that the package_data configuration was captured.
    assert 'package_data' in captured_kwargs, "'package_data' key is missing from the setup configuration."
    expected_package_data = {'': ['*', 'templates/*']}
    assert captured_kwargs['package_data'] == expected_package_data, \
        f"Expected package_data {expected_package_data}, got {captured_kwargs['package_data']}."
    # Verify that include_package_data is set to True.
    assert 'include_package_data' in captured_kwargs, "'include_package_data' key is missing from the setup configuration."
    assert captured_kwargs['include_package_data'] is True, "include_package_data should be True."
``test
import sys
import setuptools


def test_package_data_and_include_package_data(monkeypatch):
    """
    Test that the package_data and include_package_data configurations in setup.py
    are correctly set. This test replaces setuptools.setup with a dummy function to
    capture the keyword arguments passed during the setup() call and then performs assertions.
    """
    captured_kwargs = {}
    def dummy_setup(*args, **kwargs):
        nonlocal captured_kwargs
        captured_kwargs = kwargs
    # Replace setuptools.setup with dummy_setup to capture the configuration.
    monkeypatch.setattr(setuptools, 'setup', dummy_setup)
    # Remove 'setup' module from sys.modules if already imported to force re-execution.
    if 'setup' in sys.modules:
        del sys.modules['setup']
    # Import the setup.py module, which will call dummy_setup.
    import setup  # noqa: F401
    # Verify that the package_data configuration was captured.
    assert 'package_data' in captured_kwargs, "'package_data' key is missing from the setup configuration."
    expected_package_data = {'': ['*', 'templates/*']}
    assert captured_kwargs['package_data'] == expected_package_data, \
        f"Expected package_data {expected_package_data}, got {captured_kwargs['package_data']}."
    # Verify that include_package_data is set to True.
    assert 'include_package_data' in captured_kwargs, "'include_package_data' key is missing from the setup configuration."
    assert captured_kwargs['include_package_data'] is True, "include_package_data should be True."
import sys
import setuptools
import pytest


def test_setup_configuration(monkeypatch):
    """
    Test that the setup() function in setup.py is called with the correct configuration arguments.
    
    This test replaces setuptools.setup with a dummy function to capture the configuration.
    It verifies that key configuration elements such as 'name', 'version', 'install_requires', and 'entry_points'
    are set as expected.
    """
    captured_kwargs = {}
    def dummy_setup(*args, **kwargs):
        nonlocal captured_kwargs
        captured_kwargs = kwargs
    # Replace setuptools.setup with dummy_setup to capture the configuration.
    monkeypatch.setattr(setuptools, 'setup', dummy_setup)
    # Remove 'setup' module from sys.modules if already imported to force re-execution.
    if 'setup' in sys.modules:
        del sys.modules['setup']
    # Import the setup.py module, which will trigger the dummy_setup.
    import setup  # noqa: F401
    # Verify that the configuration values were captured.
    assert 'name' in captured_kwargs, "Expected 'name' to be in the setup configuration."
    assert captured_kwargs['name'] == 'bigfun', "Package name should be 'bigfun'."
    assert 'version' in captured_kwargs, "Expected 'version' in setup configuration."
    assert captured_kwargs['version'] == '0.1.0', "Package version should be '0.1.0'."
    assert 'packages' in captured_kwargs, "Expected 'packages' in the setup configuration."
    assert 'bigfun' in captured_kwargs['packages'], "Package list should include 'bigfun'."
    expected_install_requires = [
        'google-cloud-bigquery',
        'google-cloud-bigquery_connection',
        'pyyaml',
        'jinja2',
        'mkdocs-material',
        'click',
        'click-help-colors',
    ]
    assert 'install_requires' in captured_kwargs, "Expected 'install_requires' in the configuration."
    assert captured_kwargs['install_requires'] == expected_install_requires, "Install requires do not match expected values."
    assert 'entry_points' in captured_kwargs, "Expected 'entry_points' in the configuration."
    entry_points = captured_kwargs['entry_points']
    assert 'console_scripts' in entry_points, "Expected 'console_scripts' in entry_points."
    console_scripts = entry_points['console_scripts']
    # Verify that the console script entry point for 'bigfun' is included.
    assert any('bigfun = bigfun.cli:cli' in script for script in console_scripts), \
        "Console scripts should include 'bigfun = bigfun.cli:cli'."

def test_package_data_and_include_package_data(monkeypatch):
    """
    Test that the package_data and include_package_data configurations in setup.py 
    are correctly set.
    
    This test replaces setuptools.setup with a dummy function to capture the keyword arguments 
    passed to the setup() call and then asserts that package_data is set as {'': ['*', 'templates/*']}
    and include_package_data is True.
    """
    captured_kwargs = {}
    def dummy_setup(*args, **kwargs):
        nonlocal captured_kwargs
        captured_kwargs = kwargs
    # Replace setuptools.setup with dummy_setup to capture the configuration.
    monkeypatch.setattr(setuptools, 'setup', dummy_setup)
    # Remove 'setup' module from sys.modules if already imported to force re-execution.
    if 'setup' in sys.modules:
        del sys.modules['setup']
    # Import the setup.py module, which invokes dummy_setup.
    import setup  # noqa: F401
    # Verify that the package_data configuration was captured.
    assert 'package_data' in captured_kwargs, "'package_data' key is missing from the setup configuration."
    expected_package_data = {'': ['*', 'templates/*']}
    assert captured_kwargs['package_data'] == expected_package_data, \
        f"Expected package_data {expected_package_data}, got {captured_kwargs['package_data']}."
    # Verify that include_package_data is set to True.
    assert 'include_package_data' in captured_kwargs, "'include_package_data' key is missing from the setup configuration."
    assert captured_kwargs['include_package_data'] is True, "include_package_data should be True."
