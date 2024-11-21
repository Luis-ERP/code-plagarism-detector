import joblib
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

def evaluate_model(model_path, test_data_path, report_csv_path, confusion_matrix_path):
    clf = joblib.load(model_path)
    X_test, y_test = joblib.load(test_data_path)

    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    report_df.to_csv(report_csv_path, index=True)
    print(f"Classification report saved to {report_csv_path}")

    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Not Plagiarized', 'Plagiarized'])
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.savefig(confusion_matrix_path)
    print(f"Confusion matrix saved to {confusion_matrix_path}")

if __name__ == "__main__":
    model_path = r'RF_SMOTE\random_forest_model.pkl'
    test_data_path = r'RF_SMOTE\test_data.pkl'
    report_csv_path = r'RF_SMOTE\classification_report_smote.csv'
    confusion_matrix_path = r'RF_SMOTE\confusion_matrix_smote.png'

    # Evaluate the model
    evaluate_model(model_path, test_data_path, report_csv_path, confusion_matrix_path)
