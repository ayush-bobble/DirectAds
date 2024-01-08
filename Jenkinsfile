pipeline {
    agent any

    parameters {
        file(name: 'CSV_FILE', description: 'Upload your CSV file', defaultValue: 'search_queries_with_categories.csv')
    }

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
                    // Use the uploaded file in your script
                    def csvFileName = params['CSV_FILE']
                    def csvFilePath = env.WORKSPACE + '/' + csvFileName
                    
                    // Your existing logic for CSV processing
                    // ...

                    // Now you can use csvFilePath in your script
                    sh "python3 ads_keyword.py --csv-file ${csvFilePath}"
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
