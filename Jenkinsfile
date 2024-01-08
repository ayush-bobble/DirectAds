pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout(
                        [
                            $class: 'GitSCM',
                            branches: [[name: '*/main']],
                            doGenerateSubmoduleConfigurations: false,
                            extensions: [],
                            submoduleCfg: [],
                            userRemoteConfigs: [[credentialsId: '5f337acf-7604-4c6f-ad71-94bc2413b4e9', url: 'https://github.com/ayush-bobble/DirectAds.git']]
                        ]
                    )
                }
            }
        }


        stage('Run ads_keywords.py') {
            steps {
                script {
                    sh 'python3 ads_keyword.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up or post-build actions if needed
            echo 'This block is optional and can be used for clean-up actions.'
        }
    }
}