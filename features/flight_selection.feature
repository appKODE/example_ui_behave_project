# Created by juliya at 17.10.18
Feature: Here we select flight for passenger
  # Enter feature description here

  Scenario: Some chaotic actions at the screen
    # Enter steps here
    Given the screen is on
    Then assure header is on the screen
    Then assure date carousel is on the screen
    Then choose filter by price, by date
    Then find direct flight
    Then assure direct flight elements are present
    Then find the layover flight
    Then assure layover flight elements are present
    Then hit layover flight footer
    Then assure footers elements are present
    Then choose certain flight