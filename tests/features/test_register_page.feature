Feature: register on reserved website

  Scenario: test register successfully
    Given open the register page
    When the user type email testhkjdfffggh@yahoo.com
    And the user type firstname ion
    And the user type lastname ion
    And the user type password SDFGrrfg
    And the user click Create Account button
    Then the user is redirected to checkout
    And the user is logged in with ion
