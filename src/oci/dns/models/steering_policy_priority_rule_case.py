# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyPriorityRuleCase(object):
    """
    SteeringPolicyPriorityRuleCase model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyPriorityRuleCase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param case_condition:
            The value to assign to the case_condition property of this SteeringPolicyPriorityRuleCase.
        :type case_condition: str

        :param answer_data:
            The value to assign to the answer_data property of this SteeringPolicyPriorityRuleCase.
        :type answer_data: list[SteeringPolicyPriorityAnswerData]

        """
        self.swagger_types = {
            'case_condition': 'str',
            'answer_data': 'list[SteeringPolicyPriorityAnswerData]'
        }

        self.attribute_map = {
            'case_condition': 'caseCondition',
            'answer_data': 'answerData'
        }

        self._case_condition = None
        self._answer_data = None

    @property
    def case_condition(self):
        """
        Gets the case_condition of this SteeringPolicyPriorityRuleCase.

        :return: The case_condition of this SteeringPolicyPriorityRuleCase.
        :rtype: str
        """
        return self._case_condition

    @case_condition.setter
    def case_condition(self, case_condition):
        """
        Sets the case_condition of this SteeringPolicyPriorityRuleCase.

        :param case_condition: The case_condition of this SteeringPolicyPriorityRuleCase.
        :type: str
        """
        self._case_condition = case_condition

    @property
    def answer_data(self):
        """
        Gets the answer_data of this SteeringPolicyPriorityRuleCase.

        :return: The answer_data of this SteeringPolicyPriorityRuleCase.
        :rtype: list[SteeringPolicyPriorityAnswerData]
        """
        return self._answer_data

    @answer_data.setter
    def answer_data(self, answer_data):
        """
        Sets the answer_data of this SteeringPolicyPriorityRuleCase.

        :param answer_data: The answer_data of this SteeringPolicyPriorityRuleCase.
        :type: list[SteeringPolicyPriorityAnswerData]
        """
        self._answer_data = answer_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other