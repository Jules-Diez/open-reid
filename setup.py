from setuptools import setup


setup(name='open-reid',
      version='0.1.0',
      description='Deep Learning Library for Person Re-identification',
      author='Tong Xiao',
      author_email='st.cysu@gmail.com',
      url='https://github.com/Cysu/open-reid',
      license='MIT',
      install_requires=[
          'numpy', 'scipy', 'torch', 'torchvision',
          'six', 'h5py', 'Pillow',
          'scikit-learn', 'metric-learn'],
      extras_require={
          'docs': ['sphinx', 'sphinx_rtd_theme'],
      },
      packages=['reid'],
      keywords=[
          'Person Re-identification',
          'Computer Vision',
          'Deep Learning',
      ])
