# Pytest Marker Sequence
This plugin helps you sequence your markers in pytest. <br>
We mark our tests with different markers, say like nightly, sanity, stress etc. If we wish to sequence these markers for execution of our tests, we can sequence them in `pytest.ini` itself as mentioned below.
<br>
## Installation
* Plugin is available on `pypi.org` as `pip` installable.
* Install by pip command as
  ```sh
  pip install pytest-sequence-markers
  ```

<br>

## Editing `pytest.ini`
* `pytest.ini` is a configuration file for `pytest`.
* For sequencing the markers, add a section named `test_execution_sequence` in `pytest.ini`
* Add a key named `marker_sequence` and mention the sequence of the markers you want.
```ini
[pytest]
markers = sanity: Sanity Tests
    nightly: Nightly Tests
    release: Release Tests
    negative: Negative Tests
[test_execution_sequence]
marker_sequence = sanity, negative, nightly, release
```
* The sequence of markers you specify comma separated in the ini file, tests will be executed in that sequence only

<br>

## Example
* Edit the `pytest.ini` as mentioned above and mention your own sequence with own markers
* Add a test file containing all `pytest` tests

```py
import pytest


@pytest.mark.sanity
def test_sanity():
    pass

@pytest.mark.release
def test_release():
    pass


@pytest.mark.negative
def test_negative():
    pass

@pytest.mark.nightly
def test_nightly():
    pass

@pytest.mark.nightly
def test_nightly2():
    pass
```
* Execute the test with pytest command
```sh
$ pytest -sv
========================================================== test session starts ==========================================================
platform linux -- Python 3.8.10, pytest-7.3.1, pluggy-1.0.0 -- /home/siddhesh/py38/bin/python
cachedir: .pytest_cache
rootdir: /home/siddhesh/plugin_test
configfile: pytest.ini
plugins: sequence-markers-0.0.1
collecting ... I am in local one
collected 5 items

tests/test_me.py::test_sanity PASSED
tests/test_me.py::test_negative PASSED
tests/test_me.py::test_nightly PASSED
tests/test_me.py::test_nightly2 PASSED
tests/test_me.py::test_release PASSED

========================================================== 5 passed in 0.01s ==========================================================
```