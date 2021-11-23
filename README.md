# Aalto-SISU plugin for A+ LMS

This small repository implements the interactions with Aalto SISU API gateway
to connect A+ course instances with their respective SISU realisations.
The implementation extends the StudentInfoSystem class interface in A+.
See the inline documentation at the base class definition in the main
A+ repository (sis.py) for more details.

## Installation and setup

The package can be installed using pip (replace 0.2.0 with the current version
number, as can be found in this GitHub repository):

    pip install git+https://github.com/apluslms/aalto-sisu@0.2.0#egg=aalto-sisu==0.2.0

In addition, the following settings need to be applied in order to take
the plugin into use:

    # Student Information System plugin settings
    SIS_PLUGIN_MODULE = 'aalto_sisu.sis_aalto'
    SIS_PLUGIN_CLASS = 'SisuAalto'

    # Aalto-SISU SIS plugin settings
    AALTO_SISU_URL_PREFIX = 'https://course.api.aalto.fi:443/api/sisu/v1'
    AALTO_SISU_API_KEY = 'xxx'
    AALTO_SISU_ENHANCED_API_KEY = 'yyy'

where 'xxx' and 'yyy' are the API keys for the Aalto API gateway. The basic
API key can be obtained from the API gateway after you have logged in with
your Aalto account. The enhanced API key is needed for the enhanced API that
offers course teachers usernames and course participants, and needs to be
requested separately from the Aalto integration team.
