Feature: Bearing
  As the person steering
  In order to go the right direction
  I want to see the bearing towards the next mark

  @wip
  Scenario: Entering a Mark
    Given the app is running
    And my position is 81.6697 W 41.4822 N
    And I press the GOTO button
    And I enter the new mark
        | longitude | latatude  |
        | -78.8494  | 42.9047   |
    And I press Submit
    Then I see the bearing 25

  Scenario: Position Changes
    Given the app is running
    And my position is 81.23 W 41.123 N
    And I going towards the following marks
        | longitude | latatude  |
        | 81.23 W   | 41.123 N  |
        | 81.23 W   | 41.123 N  |
        | 81.23 W   | 41.123 N  |
    And my position is 81.23 W 41.123 N
    Then I see the bearing 234
    And my position is 81.23 W 41.123 N
    Then I see the bearing 223

  Scenario: Passing marks
    Given the app is running
    And my position is 81.23 W 41.123 N
    And I going towards the following marks
        | longitude | latatude  |
        | 81.23 W   | 41.123 N  |
        | 81.23 W   | 41.123 N  |
        | 81.23 W   | 41.123 N  |
    And my position is 81.23 W 41.123 N
    And my position is 81.23 W 41.123 N
    And my position is 81.23 W 41.123 N
    Then I see the bearing 12
