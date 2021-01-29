.. --------------------------------License Notice----------------------------------
.. Python Project Boilerplate - A boilerplate project for python packages
..
.. Written in 2020 by Francesco Perna
..
.. To the extent possible under law, the author(s) have dedicated all copyright
.. and related and neighboring rights to this software to the public domain
.. worldwide. This software is distributed without any warranty.
..
.. You should have received a copy of the CC0 Public Domain Dedication along
.. with this software. If not, see
.. <http://creativecommons.org/publicdomain/zero/1.0/>.
.. --------------------------------License Notice----------------------------------

A boilerplate project for python packages
#########################################

A boilerplate project to use when bootstrapping new Python 3 projects.
Copy the source code (no need to fork it), tweak the ``setup.py`` file to suit your needs and start doing things.

Features
********

* Test automation and environment provisioning using `Tox <https://tox.readthedocs.io/>`_
* Static code analysis using `Flake8 <http://flake8.pycqa.org/en/latest/>
* Unit testing using `pytest <https://docs.pytest.org/en/latest/>`_
* Enforced code coverage threshold using `coverage <https://coverage.readthedocs.io>`_
* Dependencies pinned to the major version, allowing for backwards-compatible updates when upstream
* Licensed under `CC0 Public Domain Dedication <http://creativecommons.org/publicdomain/zero/1.0/>`_,
  you can copy/paste anything and not worry about a thing, not even giving original authors attribution.

Usage
*****

<p>
  <h3>Initial Setup</h3>
  Start by creating and activate a virtual environment. <br/><br/>
  Next, Install the dependencies in requirements.txt file <br/>
  <pre><code> pip install -r requirements.txt</code></pre>
</p>
<p>

### Run the application

inside the digeiz_api run the app.py
<pre><code> python app.py</code></pre>

### Run test suite

inside the digeiz_api run the app.py
<pre><code> python -m pytest</code></pre>
