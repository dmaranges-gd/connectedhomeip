<?xml version="1.0" encoding="utf-8"?><testsuites><testsuite name="pytest" errors="14" failures="0" skipped="0" tests="14" time="0.102" timestamp="2025-04-04T13:23:38.787414-03:00" hostname="MacBook-Air-de-Diego.local"><testcase classname="" name="hello_test" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/hello_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/hello_test.py:39: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="matter_testing_infrastructure.chip.testing.taglist_and_topology_test" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/matter_testing_infrastructure/chip/testing/taglist_and_topology_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
matter_testing_infrastructure/chip/testing/taglist_and_topology_test.py:23: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="matter_testing_infrastructure.chip.testing.test_matter_asserts" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/matter_testing_infrastructure/chip/testing/test_matter_asserts.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
matter_testing_infrastructure/chip/testing/test_matter_asserts.py:6: in &lt;module&gt;
    from chip.testing import matter_asserts
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="matter_testing_infrastructure.chip.testing.test_metadata" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/matter_testing_infrastructure/chip/testing/test_metadata.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
matter_testing_infrastructure/chip/testing/test_metadata.py:19: in &lt;module&gt;
    from metadata import Metadata, MetadataReader
E   ModuleNotFoundError: No module named 'metadata'</error></testcase><testcase classname="" name="matter_testing_infrastructure.chip.testing.test_tasks" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/matter_testing_infrastructure/chip/testing/test_tasks.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
matter_testing_infrastructure/chip/testing/test_tasks.py:21: in &lt;module&gt;
    from tasks import Subprocess
E   ModuleNotFoundError: No module named 'tasks'</error></testcase><testcase classname="" name="test_plan_table_generator" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_plan_table_generator.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_plan_table_generator.py:24: in &lt;module&gt;
    import click
E   ModuleNotFoundError: No module named 'click'</error></testcase><testcase classname="" name="test_testing.test_IDM_10_4" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_IDM_10_4.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_IDM_10_4.py:22: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_CCNTL_2_2" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_CCNTL_2_2.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_CCNTL_2_2.py:26: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_DGGEN_3_2" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_DGGEN_3_2.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_DGGEN_3_2.py:23: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_ICDM_2_1_full_pics" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_ICDM_2_1_full_pics.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_ICDM_2_1_full_pics.py:21: in &lt;module&gt;
    from common_icdm_data import ICDMData, c, run_tests, uat
test_testing/common_icdm_data.py:23: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_ICDM_2_1_min_pics" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_ICDM_2_1_min_pics.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_ICDM_2_1_min_pics.py:21: in &lt;module&gt;
    from common_icdm_data import ICDMData, c, run_tests
test_testing/common_icdm_data.py:23: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_MCORE_FS_1_1" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_MCORE_FS_1_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_MCORE_FS_1_1.py:26: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_SC_7_1" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_SC_7_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_SC_7_1.py:23: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase><testcase classname="" name="test_testing.test_TC_TMP_2_1" time="0.000"><error message="collection failure">ImportError while importing test module '/Users/diegomaranges/Documents/connectedhomeip/src/python_testing/test_testing/test_TC_TMP_2_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
../../config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/config/ameba/third_party/connectedhomeip/src/python_testing/test_testing/test_TC_TMP_2_1.py:24: in &lt;module&gt;
    import chip.clusters as Clusters
E   ModuleNotFoundError: No module named 'chip'</error></testcase></testsuite></testsuites>