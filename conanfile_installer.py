# -*- coding: utf-8 -*-

import os
from conanfile_base import BisonBase


class BisonInstaller(BisonBase):
    settings = "os_build", "arch_build", "compiler"
    exports = BisonBase.exports + ["conanfile_base.py"]
    name = "bison_installer"
    version = BisonBase.version
    
    def package_id(self):
        del self.info.settings.compiler

    def package_info(self):
        bison_pkgdir = os.path.join(self.package_folder, "share", "bison")
        self.output.info('Setting BISON_INSTALLER_PKGDATADIR environment variable: {}'.format(bison_pkgdir))
        self.env_info.BISON_PKGDATADIR = bison_pkgdir
        
        bindir = os.path.join(self.package_folder, "bin")
        self.output.info('Appending PATH environment variable: {}'.format(bindir))
        self.env_info.PATH.append(bindir)

        self.output.info('Setting BISON_INSTALLER_ROOT environment variable: {}'.format(self.package_folder))
        self.env_info.BISON_INSTALLER_ROOT = self.package_folder
