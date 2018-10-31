# Created by juliya at 18.10.18
Feature: Tariff back selection
  # Enter feature description here

  Scenario: Here user chooses back tariff
    # Enter steps here
  Given the screen is on
    Then assure header is on the screen
    Then assure tariff back list elements are ok
    Then click tariffs options
    Then assure tariffs options ok
    Then assure tariffs sum and common sum are equal
    Then user clicks Next