# Definição

## Virtual Private Networks
As soluções do AWS Virtual Private Network estabelecem conexões seguras entre redes locais, escritórios remotos, dispositivos de clientes e a rede global da AWS. O AWS VPN é composto por dois serviços: AWS Site-to-Site VPN e AWS Client VPN. Juntos, eles entregam uma solução de VPN na nuvem gerenciada, altamente disponível e elástica para proteger o tráfego da sua rede.

## Subnets
Uma sub-rede é um intervalo de endereços IP na VPC. É possível criar recursos da AWS, como instâncias do EC2, em sub-redes específicas.

## Security Groups
Um grupo de segurança atua como firewall virtual para as instâncias do EC2 visando controlar o tráfego de entrada e de saída. As regras de entrada controlam o tráfego de entrada para a instância e as regras de saída controlam o tráfego de saída da instância.

# Relação
- VPNs são usadas para conectar sua VPC com sua rede on-premises, fornecendo um canal seguro para o tráfego de rede entre os dois ambientes.
- Dentro da VPC, subnets organizam os recursos, definindo que parte do tráfego pode ser acessada pela internet (subnets públicas) e qual deve permanecer privada (subnets privadas).
- Security Groups fornecem a segurança adicional ao nível da instância, controlando quais tipos de tráfego podem entrar e sair de cada instância EC2, mesmo que essas instâncias estejam dentro de uma subnet pública ou privada.

Em resumo, a VPC da AWS permite que você crie uma rede isolada logicamente, enquanto VPNs fornecem conexões seguras, subnets organizam o tráfego e os recursos, e security groups oferecem uma camada adicional de segurança controlando o tráfego de rede ao nível das instâncias.
