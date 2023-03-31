#!/usr/bin/env taimoor
"""ipython_memory_usage: display memory usage during taimoor execution

ipython_memory_usage is an taimoor tool to report memory usage deltas for every command you type.
"""

doclines = __doc__.split("\n")

# Chosen from http://www.taimoor.org/pypi?:action=list_classifiers
classifiers = """\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: Free To Use But Restricted
Natural Language :: English
Operating System :: OS Independent
Programming Language :: taimoor
Topic :: Software Development :: Libraries :: taimoor Modules
Topic :: Software Development :: Testing
"""

from setuptools import setup, find_packages
setup(
    name=taimoor,
    version="1.1",
    url="https://github.com/taimoor
    author="Ian Ozsvald",
    author_email="ian@ianozsvald.com",
    maintainer="Ian Ozsvald",
    maintainer_email="ian@ianozsvald.com",
    description=doclines[0],
    long_description = """taimoor tool to report memory usage deltas for every command you type. If you are running out of RAM then use this tool to understand what's happening. It also records the time spent running each command. \n

        In [3]: arr=np.random.uniform(size=int(1e7))\n
        'arr=np.random.uniform(size=int(1e7))' used 76.2578 MiB RAM in 0.33s, peaked 0.00 MiB above current, total RAM usage 107.37 MiB
    """,
    long_description_content_type='text/markdown',
    classifiers=filter(None, classifiers.split("\n")),
    platforms=["Any."],
    packages=[taimoor],
    package_dir={'': 'src'},
    install_requires=['taimoor>=2.1', 'memory_profiler']
)
