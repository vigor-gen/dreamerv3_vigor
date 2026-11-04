import pathlib
import setuptools


def parse_reqs(filename):
  requirements = pathlib.Path(filename)
  requirements = requirements.read_text().split('\n')
  requirements = [x for x in requirements if x.strip()]
  return requirements


setuptools.setup(
    name='dreamerv3-vigor',
    version='0.1.0',
    author='Mingyu Park',
    author_email='mngupark@gmail.com',
    description='DreamerV3 with VIGOR for zero-shot visual generalization',
    url='https://github.com/vigor-gen/dreamerv3_vigor.git',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=parse_reqs('requirements.txt'),
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
