<VirtualHost *:80>

    ServerName jqwiki.com
    ServerAdmin phawksworth@gmail.com
  
    LogLevel warn
    ErrorLog /var/log/apache2/jqwiki.com.error.log
    CustomLog /var/log/apache2/jqwiki.com.access.log combined
    LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i \" \"%{Cookie}i\""

    <Directory /var/www/jqwiki.com>
        Order deny,allow
        Allow from all
    </Directory>
    
    DocumentRoot /var/www/jqwiki.com/
    
</VirtualHost>