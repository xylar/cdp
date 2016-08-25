import os, sys
import collections
import logging
import json
from CDP.base.CDPDriver import *

class PMPDriver(CDPDriver):

    def check_parameter(self):
        #check that all of the variables used from parameter exist
        PMPDriverCheckParameter.check_parameter(self.parameter)

    def run_diags(self):
        run = PMPDriverRunDiags(self.parameter)
        run.run_diags()

    def export(self):
        pass