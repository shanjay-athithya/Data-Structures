class TreeNode:
    def _init_(self, feature=None, value=None, label=None):
        self.feature = feature  # Feature to split on at this node
        self.value = value  # Feature value to compare at this node
        self.label = label  # Output label for leaf node
        self.children = []  # List of child nodes

    def add_child(self, child):
        self.children.append(child)

    def is_leaf(self):
        return len(self.children) == 0


def construct_decision_tree(features, feature_values, rules, output_labels):
    root = TreeNode()

    def build_tree(node, rule_set):
        if len(rule_set) == 1:  # Leaf node
            node.label = output_labels[rule_set[0]]
        else:
            best_feature = None
            best_value = None
            best_score = 0

            for feature in features:
                for value in feature_values[feature]:
                    pos_examples = []
                    neg_examples = []

                    for rule_idx in rule_set:
                        rule = rules[rule_idx]
                        if rule[feature] == value:
                            pos_examples.append(rule_idx)
                        else:
                            neg_examples.append(rule_idx)

                    score = calculate_score(pos_examples, neg_examples)

                    if score > best_score:
                        best_score = score
                        best_feature = feature
                        best_value = value

            if best_feature is None:  # No further splitting possible
                majority_label = find_majority_label(rule_set)
                node.label = output_labels[majority_label]
            else:
                node.feature = best_feature
                node.value = best_value

                pos_examples = []
                neg_examples = []

                for rule_idx in rule_set:
                    rule = rules[rule_idx]
                    if rule[best_feature] == best_value:
                        pos_examples.append(rule_idx)
                    else:
                        neg_examples.append(rule_idx)

                pos_child = TreeNode()
                build_tree(pos_child, pos_examples)
                node.add_child(pos_child)

                neg_child = TreeNode()
                build_tree(neg_child, neg_examples)
                node.add_child(neg_child)

    build_tree(root, range(len(rules)))
    return root


# Helper functions for scoring and finding majority label

def calculate_score(pos_examples, neg_examples):
    # Your scoring function implementation here
    pass


def find_majority_label(rule_set):
    # Your implementation to find the majority label here
    pass


# Example usage
features = ['color', 'size']
feature_values = {
    'color': ['red', 'green', 'blue'],
    'size': ['small', 'medium', 'large']
}
rules = [
    {'color': 'red', 'size': 'small'},
    {'color': 'red', 'size': 'medium'},
    {'color': 'green', 'size': 'medium'},
    {'color': 'blue', 'size': 'large'},
    # ... more rules ...
]
output_labels = ['A', 'B', 'C']

decision_tree = construct_decision_tree(features, feature_values, rules, output_labels)

# Use the decision tree for prediction or other purposes