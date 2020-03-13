first_test="ui_tests/ui_profile_automation.py"
skip="ui_tests/selenium_helper.py"
eval "./runUITests.sh $first_test"
for file in $(ls ui_tests/*.py); do
    if [ "$file" != "$first_test" ] && [ "$file" != "$skip" ]; then
        eval "./runUITests.sh $file"
        sleep 1
    fi
done
