# Created by Work at 9/22/2023
Feature: Shields protect the ship when they are charged and raised

  Scenario: Attack reduces shield to 0 and lowers it
    Given Shield level is at 1000
    And Shield is "raised"

    When Ship is hit with a 1000 energy attack

    Then we expect Shield level to be 0
    And Shield should be "down"
    And no subsystems are damaged