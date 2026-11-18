import numpy as np

class Node:
        return self.value is not None


class DecisionTreeFromScratch:
        return self._traverse_tree(x, node.right)


# --- Example Usage ---
if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split

    # Load dataset
    data = load_iris()
    X, y = data.data, data.target

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train our custom model
    clf = DecisionTreeFromScratch(max_depth=10)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)

    # Calculate performance accuracy
    accuracy = np.sum(y_test == predictions) / len(y_test)
    print(f"Custom Decision Tree Accuracy: {accuracy * 100:.2f}%")
