# Created by juliya at 16.10.18
Feature: Booking first screen operations
  # Enter feature description here

  Scenario: Do date, city, passengers changes
    # Enter steps here
    Given the screen is open
    Then user chooses date of flight
    Then user chooses cities
    Then user chooses passengers
    Then user clicks Next