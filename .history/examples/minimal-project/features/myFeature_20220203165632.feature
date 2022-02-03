  # minimal-project/features/myFeature.feature
  Feature: Sample Snippets test
  As a developer
  I should be able to use given text snippets

  Scenario: open URL
      Given the page url is not "http://webdriverjs.christian-bromann.com/"
      And   I open the url "http://google.com"

  Scenario: click on link
      When  I click on the link "Store"
      Then  I expect that the title is "Google Store for Google Made Devices & Accessories"
