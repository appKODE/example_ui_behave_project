# Created by juliya at 16.10.18
Feature: Booking first screen operations
  # Enter feature description here

  Scenario: Do date, city, passengers changes
    # Enter steps here
    Given the screen is open
    Then user closes profile sign
    Then user chooses booking tab
    Then user chooses date of flight to
    Then user chooses date of flight back
    Then user chooses city from
    Then user chooses city to
    Then user chooses passengers
    Then user clicks Next