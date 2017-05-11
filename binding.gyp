{
    'target_defaults': {
        'default_configuration': 'Release_x64',
        'configurations': {
            'Debug': {
                # configuration specific settings
            },
            'Release': {
                # configuration specific settings
            },
            'Debug_x64': {
                'inherit_from': ['Debug'],
                'msvs_configuration_platform': 'x64',
            },
            'Release_x64': {
                'inherit_from': ['Release'],
                'msvs_configuration_platform': 'x64',
            },
        },
    },
    "targets": [
        {
            "cflags": ["-Fo=$(IntDir)/%(RelativeDir)/"],
            "include_dirs": [
            ],
            "type": "shared_library",
            "target_name": "pvpkcs11",
            "libraries": [
                "Crypt32.lib",
                "Bcrypt.lib",
                "Ncrypt.lib",
            ],
            "msvs_settings": {
                "VCCLCompilerTool": {
                    "ObjectFile": "$(IntDir)/%(RelativeDir)/"  # /Fo
                },
            },
            "sources": [
                # core
                "src/stdafx.cpp",
                "src/pkcs11.cpp",
                "src/core/crypto.h",
                "src/core/crypto_digest.cpp",
                "src/core/crypto_sign.cpp",
                "src/core/crypto_encrypt.cpp",
                "src/core/excep.h",
                "src/core/excep.cpp",
                "src/core/module.h",
                "src/core/module.cpp",
                "src/core/object.h",
                "src/core/object.cpp",
                "src/core/session.h",
                "src/core/session.cpp",
                "src/core/slot.h",
                "src/core/slot.cpp",
                "src/core/template.cpp",
                "src/core/objects/mechanism.cpp",
                "src/core/objects/storage.cpp",
                "src/core/objects/key.cpp",
                "src/core/objects/private_key.cpp",
                "src/core/objects/public_key.cpp",
                "src/core/objects/secret_key.cpp",
                "src/core/objects/aes_key.cpp",
                "src/core/objects/rsa_private_key.cpp",
                "src/core/objects/rsa_public_key.cpp",
                "src/core/objects/ec_key.cpp",
                "src/core/objects/certificate.cpp",
                "src/core/objects/x509_certificate.cpp",
                # mscapi
                "src/mscapi/helper.cpp",
                "src/mscapi/session.cpp",
                "src/mscapi/slot.cpp",
                "src/mscapi/key.cpp",
                "src/mscapi/rsa.cpp",
                "src/mscapi/ec.cpp",
                "src/mscapi/aes.cpp",
                # mscapi/crypto
                "src/mscapi/crypto_digest.cpp",
                "src/mscapi/crypto_sign.cpp",
                "src/mscapi/crypto_encrypt.cpp",
                # mscapi/bcrypt
                "src/mscapi/bcrypt/algorithm.cpp",
                "src/mscapi/bcrypt/key.cpp",
                # mscapi/ncrypt
                "src/mscapi/ncrypt/provider.cpp",
                "src/mscapi/ncrypt/key.cpp"
            ]
        }
    ]
}
