# Created by juliya at 18.10.18
Feature: Tariff selection
  # Enter feature description here

  Scenario: Here user chooses tariff
    # Enter steps here
  Given the screen is on
    Then assure header is on the screen
    Then assure tariff list elements are ok
    Then click tariffs options
    Then assure tariffs options ok
    Then assure tariffs sum and common sum are equal
    Then user clicks Next