from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'HttpClient'
    version = 'c8507fd'
    url = 'https://github.com/hicktech/conan-HttpClient'
    repo_url = 'https://github.com/nmattisson/HttpClient.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src', excludes='*examples*')
        self.copy('*.h*', dst='include', excludes='*examples*')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
