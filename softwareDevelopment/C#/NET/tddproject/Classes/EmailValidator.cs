namespace Classes;

public class EmailValidator
{
    public static bool ValidateEmail(string email)
    {
        if (string.IsNullOrWhiteSpace(email))
        {
            return false;
        }

        var emailParts = email.Split('@');
        if (emailParts.Length != 2)
        {
            return false;
        }

        var localPart = emailParts[0];
        var domainPart = emailParts[1];

        if (string.IsNullOrWhiteSpace(localPart) || string.IsNullOrWhiteSpace(domainPart))
        {
            return false;
        }

        if (localPart.Length > 64 || domainPart.Length > 255)
        {
            return false;
        }

        if (localPart.Contains("..") || domainPart.Contains(".."))
        {
            return false;
        }

        if (localPart.StartsWith(".") || localPart.EndsWith(".") || domainPart.StartsWith(".") || domainPart.EndsWith("."))
        {
            return false;
        }

        if (localPart.Contains(".@") || domainPart.Contains(".@"))
        {
            return false;
        }

        if (localPart.Contains("@.") || domainPart.Contains("@."))
        {
            return false;
        }

        if (localPart.Contains("."))
        {
            var localPartParts = localPart.Split('.');
            foreach (var part in localPartParts)
            {
                if (string.IsNullOrWhiteSpace(part))
                {
                    return false;
                }
            }
        }

        return true;
    }
}
